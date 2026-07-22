<script setup lang="ts">
defineProps<{
  title: string
  value: string | number
}>()
</script>

<template>
  <div class="queue-card">
    <span class="title">
      {{ title }}
    </span>

    <h2>
      {{ value }}
    </h2>
  </div>
</template>

<style scoped>
.queue-card {
  display: flex;

  flex-direction: column;

  justify-content: center;

  min-height: 110px;

  padding: 20px;

  border: 1px solid #e2e8f0;

  border-radius: 14px;

  background: white;
}

.title {
  color: var(--text-secondary);

  font-size: 14px;

  font-weight: 500;
}

h2 {
  margin-top: 14px;

  color: var(--text-primary);

  font-size: 52px;

  font-weight: 700;

  line-height: 1;
}
</style>
