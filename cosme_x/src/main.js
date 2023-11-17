import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import 'quasar/dist/quasar.css';
import { Quasar, QTabs, QTab, QRouteTab, QCard, QBtn, QImg, QRadio, QIcon, QList, QItem, QItemSection,QCardSection } from 'quasar';
import '@quasar/extras/mdi-v7/mdi-v7.css';

const app = createApp(App)
app.use(Quasar, {
    components: {
        QTabs,
        QTab,
        QRouteTab,
        QCard,
        QBtn,
        QImg,
        QRadio,
        QIcon,
        QList,
        QItem,
        QItemSection,
        QCardSection
    }
})
app.use(store)
app.use(router)
app.mount("#app");

