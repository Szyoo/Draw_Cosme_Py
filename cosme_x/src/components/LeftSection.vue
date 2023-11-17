<template>
    <!-- Left: Prize Info -->
    <div class="left">
        <h5 class="q-my-sm">当前奖品</h5>
        <div class="prize-details">
            <q-card class="my-card">
                <q-img :src="prizeImage" placeholder-src="https://via.placeholder.com/150" />
                <q-card-section>
                    <div class="text-subtitle1">{{ prizeTitle || '奖品信息待加载...' }}</div>
                    <div class="text-subtitle2">{{ prizeDescription || '奖品详情待加载...' }}</div>
                </q-card-section>
            </q-card>
        </div>

        <div class="options-section" ref="optionsSection">
            <!-- 如果有 prizeOptions 数据，显示实际的选项 -->
            <div class="options-container" v-if="prizeOptions && prizeOptions.length">
                <div v-for="option in prizeOptions" :key="option.id" class="option flex-container">
                    <q-radio v-model="selectedOption" :val="option.id" :label="option.text"></q-radio>
                </div>
            </div>

            <!-- 如果没有 prizeOptions 数据，显示两个占位符选项 -->
            <div class="options-container" v-else>
                <div class="option flex-container">
                    <q-radio disabled label=" " :val="null" :modelValue="null"></q-radio>
                    <div class="option-placeholder"></div>
                </div>
                <div class="option flex-container">
                    <q-radio disabled label=" " :val="null" :modelValue="null"></q-radio>
                    <div class="option-placeholder"></div>
                </div>
            </div>

            <!-- 提交按钮，仅当有选项且已选择一个选项时可用 -->
            <q-btn :disabled="!selectedOption" class="q-mt-md" color="grey" label="确认" @click="confirmOption" />

            <!-- Grey Overlay -->
            <div v-if="!optionsAvailable || !running" class="overlay"></div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        running: {
            type: Boolean,
            default: false
        },
    },
    data() {
        return {
            socket: null,
            selectedOption: null,
            prizeImage: null,
            prizeTitle: null,
            prizeDescription: null,
            prizeOptions: [
                // { id: 1, text: '商品A: 这是一个比较长的商品名称，用于测试排版效果abcd\n123' },
                // { id: 2, text: '商品B' },
                // { id: 3, text: '商品C' },
                // { id: 4, text: '商品D' },
                // { id: 5, text: '商品D' },
                // { id: 6, text: '商品D' },
            ],
            optionsAvailable: false
        };
    },
    created() {
        this.initWebSocket();
    },
    methods: {
        initWebSocket() {
            this.socket = new WebSocket('ws://localhost:8000/ws');

            this.socket.onmessage = (event) => {
                let data = JSON.parse(event.data);
                if (data.type === 'prizeInfo') {
                    this.prizeImage = data.payload.image;
                    this.prizeTitle = data.payload.title;
                    this.prizeDescription = data.payload.description;
                    // 清除旧的选项
                    this.prizeOptions = [];
                    this.optionsAvailable = false;
                } else if (data.type === 'options') {
                    this.prizeOptions = data.payload.options;
                    this.optionsAvailable = this.running && this.prizeOptions.length > 0;
                }
            };

            this.socket.onclose = (event) => {
                console.log('WebSocket closed:', event);
            };

            this.socket.onerror = (error) => {
                console.error('WebSocket Error:', error);
            };
        },
        confirmOption() {
            if (this.selectedOption && this.socket.readyState === WebSocket.OPEN) {
                this.socket.send(JSON.stringify({
                    type: 'submitChoice',
                    payload: { selectedOption: this.selectedOption }
                }));
            }
        }
    },
    watch: {
        prizeImage(newVal, oldVal) {
            if (newVal !== oldVal) {
                this.prizeOptions = [];
                this.optionsAvailable = false;
            }
        },
        prizeTitle(newVal, oldVal) {
            if (newVal !== oldVal) {
                this.prizeOptions = [];
                this.optionsAvailable = false;
            }
        },
        running(newVal) {
            this.optionsAvailable = newVal && this.prizeOptions.length > 0;
        }
    }
};
</script>

<style scoped>
/* 主容器样式 */
.left {
    display: flex;
    flex-direction: column;
    height: calc(100vh - 48px);
}

/* 奖品详情样式 */
.prize-details {
    padding: 16px;
    max-width: 300px;
    width: 100%;
}

/* 选项部分样式 */
.options-section {
    position: relative;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 32px;
    max-width: 300px;
    width: 100%;
    overflow-y: auto;
}

.options-container {
    overflow-y: auto;
    max-height: 100%;
    /* 使其不超过父容器的高度 */
}

/* 选项背景伪元素样式 */
.options-section::before {
    content: "";
    /* 这是必要的，以便伪元素可以显示 */
    position: absolute;
    top: 16px;
    right: 16px;
    bottom: 16px;
    left: 16px;
    background-color: #f3f3f3;
    /* 替换为您所需的颜色 */
    border-radius: 10px;
    z-index: -1;
    /* 确保它位于内容之下 */
}


/* 选项样式 */
.option {
    display: flex;
    align-items: center;
    text-align: left;
}

.option-placeholder {
    background: #d3d3d3;
    border-radius: 10px;
    height: 1.5rem;
    margin-left: 1rem;
    flex-grow: 1;
}

/* 灰色遮罩层样式 */
.overlay {
    position: absolute;
    top: 16px;
    right: 16px;
    bottom: 16px;
    left: 16px;
    background-color: rgba(220, 220, 220, 0.3);
    border-radius: 10px;
    z-index: 10;
}
</style>
