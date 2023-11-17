<template>
    <!-- Middle: Control Center -->
    <div class="center">
        <!-- <q-img style="width: 200px; height: 200px;" :src="logo" /> -->
        <div class="q-my-sm text-h4">WELCOME TO</div>
        <div class="q-my-sm text-h2 glowing-text text-weight-bolder">COSME X</div>
        <div class="q-my-md text-subtitle1">As an @COSME™'s Presents Draw Scripts<br>Hoping to Bring U Beauty and Luck</div>
        <div class="gear-container" @mouseover="hoverGear" @mouseleave="leaveGear">
            <div class="gear-background" v-if="showBackground"></div>
            <q-icon ref="gearIcon" name="mdi-cog-outline"
                :class="{ 'settings-icon': true, 'rotate-gear': rotating, 'reverse-rotate-gear': reverseRotating }"
                @click="goToSettings" color="grey" size="3em" />
        </div>
        <template class="below">
            <q-btn class="q-my-md" color="secondary" label="开始" v-if="!running" @click="startDraw" />
            <q-btn class="q-my-md" color="red" label="停止" v-else @click="stopDraw" />
            <!-- <button class="q-my-sm" v-if="!running" @click="startDraw">开始</button>
            <button class="q-my-sm" v-else @click="stopDraw">停止</button> -->

            <div class="info">
                <p class="q-my-xs">Chrome 版本: {{ chromeVersion }}</p>
                <p class="q-my-xs">ChromeDriver 版本: {{ chromeDriverVersion }}</p>
                <p class="q-my-xs">作者: Szyyw</p>
            </div>
        </template>
    </div>
</template>

<script>
import logo from "@/assets/logo.png"
import { ipcRenderer } from 'electron';

export default {
    props: {
        running: {
            type: Boolean,
            default: false
        },
    },
    data() {
        return {
            logo,
            chromeDriverVersion: "Unknown",
            colors: ['#EE7752', '#E73C7E', '#23A6D5', '#23D5AB'],
            rotating: false,
            reverseRotating: false, // 新的数据属性，用于控制反向旋转
            showBackground: false
        };
    },
    computed: {
        glowingTextStyle() {
            const shuffledColors = this.shuffleColors(this.colors);
            const background = `linear-gradient(45deg, ${shuffledColors.join(', ')})`;
            return {
                fontSize: '2em',
                textAlign: 'center',
                color: '#fff',
                background,
                backgroundSize: '200% 200%',
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
                animation: 'gradient 6s linear infinite'
            };
        },

        chromeVersion() {
            return this.$store.state.chromeVersion || 'Unknown';  // 如果 Vuex store 中没有版本信息，则返回 'Unknown'
        }
    },
    methods: {
        startDraw() {
            this.$emit("update:running", true);
            // Call your backend to start the draw
            // fetch('/start-draw/', { method: 'POST' })
            //     .then(response => response.json())
            //     .then(data => {
            //         console.log(data);  // 打印后端的响应，确认抽奖是否已启动
            //     });
        },
        stopDraw() {
            this.$emit("update:running", false);
            // Call your backend to stop the draw
            // fetch('/stop-draw/', { method: 'POST' })
            //     .then(response => response.json())
            //     .then(data => {
            //         console.log(data);  // 打印后端的响应，确认抽奖是否已停止
            //     });
        },
        hoverGear() {
            this.rotating = true;
            this.reverseRotating = false;  // 确保反向旋转被关闭
            this.showBackground = true;
        },
        leaveGear() {
            this.rotating = false;
            this.reverseRotating = true;  // 启动反向旋转

            // 将背景的消失独立出来，使其立即消失
            this.showBackground = false;

            setTimeout(() => {
                this.reverseRotating = false;  // 旋转完成后，关闭反向旋转
            }, 1000);  // 1秒后执行，与旋转动画的持续时间匹配
        },
        goToSettings() {
            this.$router.push({ name: 'settings' });
        },
    },
    mounted() {
        // 首先，检查 Vuex 中是否已经有了 chromeDriverVersion 的值
        if (!this.$store.state.chromeDriverVersion) {
            // 如果 Vuex 中没有值，那么从后端获取
            fetch('/get-chromedriver-version')
                .then(response => response.text())
                .then(data => {
                    this.chromedriverVersion = data.trim();  // 使用 trim() 去除可能的空格或换行符
                    this.$store.dispatch('updateChromeDriverVersion', this.chromedriverVersion);
                });
        } else {
            // 如果 Vuex 中有值，直接使用那个值
            this.chromedriverVersion = this.$store.state.chromeDriverVersion;
        }

        ipcRenderer.on('chrome-version', (event, version) => {
            this.$store.dispatch('updateChromeVersion', version);
        });
    },

    beforeUnmount() {
        ipcRenderer.removeAllListeners('chrome-version');
    },
};
</script>

<style>
/* 主容器样式 */
.center {
    display: flex;
    flex-direction: column;
    align-items: center;
}

@keyframes gradient {
    0% {
        background-position: 0% 50%;
    }

    100% {
        background-position: 100% 50%;
    }
}

.glowing-text {
    color: #fff;
    background: linear-gradient(45deg, #EE7752, #E73C7E, #23A6D5, #23D5AB, #EE7752, #E73C7E, #23A6D5, #23D5AB);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradient 6s linear infinite;
    /* Adjust the animation duration here */
}

.gear-container {
    position: relative;
    display: inline-block;
    padding: 5px;
    cursor: pointer;
}

.gear-background {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #f3f3f3;
    border-radius: 8px;
    z-index: -1;
}

@keyframes rotateForward {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(180deg);
    }
}

@keyframes rotateBackward {
    0% {
        transform: rotate(180deg);
    }

    100% {
        transform: rotate(0deg);
    }
}

.settings-icon.rotate-gear {
    animation-name: rotateForward;
    animation-duration: 1s;
    /* 增加持续时间以实现更慢的旋转 */
    animation-fill-mode: forwards;
}

.settings-icon.reverse-rotate-gear {
    animation-name: rotateBackward;
    animation-duration: 1s;
    /* 增加持续时间以实现更慢的旋转 */
    animation-fill-mode: forwards;
}



/* 选项部分样式 */
.below {
    position: relative;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding-left: 32px;
    padding-right: 32px;
    padding-bottom: 16px;
}
</style>