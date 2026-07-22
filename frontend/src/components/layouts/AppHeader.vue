<script setup lang="ts">
defineProps<{
  shopName: string
}>()
</script>

<template>
  <header class="header">
    <h1>QLine</h1>

    <p>{{ shopName }}</p>
  </header>
</template>

<style scoped>
.header {
  margin-bottom: 28px;
  text-align: center;
}

.header h1 {
  margin: 0;

  color: var(--primary);

  font-size: 36px;

  font-weight: 700;

  line-height: 1.2;
}

.header p {
  margin-top: 8px;

  color: var(--text-secondary);

  font-size: 15px;
}
</style>
