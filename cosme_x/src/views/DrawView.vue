<template>
  <div class="draw-container">
    <left-section class="section" :running="running"></left-section>
    <center-section class="section" :running="running" @update:running="running = $event"></center-section>
    <right-section class="section" :running="running"></right-section>
  </div>
</template>

<script>
import LeftSection from '@/components/LeftSection.vue';
import CenterSection from '@/components/CenterSection.vue';
import RightSection from '@/components/RightSection.vue';

export default {
  components: {
    LeftSection,
    CenterSection,
    RightSection
  },
  data() {
    return {
      running: false,
    };
  },
};
</script>

<style scoped>
.draw-container {
  display: flex;
  flex-direction: row;
}

.section {
  flex: 1;
  height: calc(100vh - 48px);
  align-items: center;
}
</style>
