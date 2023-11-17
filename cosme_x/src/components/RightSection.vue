<template>
    <div class="right">
        <h5 class="q-my-sm">运行状态</h5>
        <!-- Right: Logs -->
        <div class="log-section">
            <div class="log-container">
                <div class="log-grid">
                    <template v-for="entry in logs" :key="entry.datetime">
                        <div class="date-cell">{{ entry.datetime.split(' ')[0] }}</div>
                        <div class="time-cell">{{ entry.datetime.split(' ')[1] }}</div>
                        <div class="text-cell">{{ entry.text }}</div>
                    </template>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "RightSection",
    props: {
        running: {
            type: Boolean,
            default: false
        },
    },
    data() {
        return {
            logs: [],
            // logs: [
            //     { datetime: "08-11 09:00:00", text: "开始运行" },
            //     { datetime: "08-11 09:01:00", text: "开始检测" },
            //     { datetime: "08-11 09:02:00", text: "检测到X个\n1.xxx\n2.xxx" },
            //     { datetime: "08-11 10:00:00", text: "开始抽取1" },
            //     { datetime: "08-11 10:03:00", text: "开始1" },
            //     { datetime: "08-11 10:05:00", text: "开始2" },
            //     { datetime: "08-12 09:00:00", text: "开始运行" },
            //     { datetime: "08-12 09:01:00", text: "开始检测" },
            //     { datetime: "08-12 09:02:00", text: "检测到X个\n1.xxx\n2.xxx" },
            //     { datetime: "08-12 10:00:00", text: "开始抽取1" },
            //     { datetime: "08-12 10:03:00", text: "开始1" },
            //     { datetime: "08-12 10:05:00", text: "开始2" },
            //     { datetime: "08-13 09:00:00", text: "开始运行" },
            //     { datetime: "08-13 09:01:00", text: "开始检测" },
            //     { datetime: "08-13 09:02:00", text: "检测到X个\n1.xxx\n2.xxx" },
            //     { datetime: "08-13 10:00:00", text: "开始抽取1" },
            //     { datetime: "08-13 10:03:00", text: "开始1" },
            //     { datetime: "08-13 10:05:00", text: "开始2" },
            // ],
            socket: null,
        };
    },
    watch: {
        // running() {
        running(newVal) {
            if (newVal) {
                // 当 running 为 true 时，开始连接并监听 WebSocket
                this.logs = [];  // 清空现有日志
                this.initWebSocket();
            } else {
                // 当 running 为 false 时，断开 WebSocket 连接
                if (this.socket) {
                    this.socket.close();
                    this.socket = null;
                }
            }
        }
        // },
    },
    // created() {
    //     this.initWebSocket();
    // },
    methods: {
        initWebSocket() {
            if (!this.socket) {
                this.socket = new WebSocket('ws://localhost:8000/ws');

                this.socket.addEventListener('open', (event) => {
                    console.log('WebSocket connection opened:', event);
                });

                this.socket.addEventListener('error', (event) => {
                    console.log('WebSocket error:', event);
                });

                this.socket.onmessage = (event) => {
                    console.log('Message from server:', event.data);
                    const data = JSON.parse(event.data);
                    if (data.type === "new_log") {
                        console.log(data.message);  // 或者执行其他操作，如在页面上显示消息
                        this.logs.push(data.message);
                    }
                };

                this.socket.addEventListener('close', (event) => {
                    console.log('WebSocket connection closed:', event);
                    const currentTime = this.formatDateTime(new Date());
                    const logMessage = {
                        datetime: currentTime,
                        text: "已断开连接"
                    };
                    this.logs.push(logMessage);
                });

                // 滚动到底部
                this.$nextTick(() => {
                    const logList = this.$refs.logList;
                    logList.scrollTop = logList.scrollHeight;
                });
            }
        },
        formatDateTime(date) {
            const day = String(date.getDate()).padStart(2, '0');
            const month = String(date.getMonth() + 1).padStart(2, '0'); // Months are 0-indexed
            const hours = String(date.getHours()).padStart(2, '0');
            const minutes = String(date.getMinutes()).padStart(2, '0');
            const seconds = String(date.getSeconds()).padStart(2, '0');

            return `${month}-${day} ${hours}:${minutes}:${seconds}`;
        }
    },
    beforeUnmount() {
        // 关闭WebSocket连接
        if (this.socket) {
            this.socket.close();
        }
    }
};
</script>
<style>
.right {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding-left: 16px;
    padding-right: 16px;
    padding-bottom: 16px;
    height: calc(100vh - 48px);
}

.log-section {
    flex: 1;
    width: 100%;
    max-width: 300px;
    background: #F5F5F5;
    border-radius: 10px;
    padding: 16px;
    overflow-y: auto;
}

.log-container {
    width: 100%;
    height: 100%;
    overflow-y: auto;
}

.log-grid {
    display: grid;
    grid-template-columns: auto auto 1fr;
    gap: 5px;
    width: 100%;
}

.date-cell,
.time-cell,
.text-cell {
    padding: 2.5px;
    text-align: left;
    white-space: pre-line;
}
</style>