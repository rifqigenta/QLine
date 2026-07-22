<script setup lang="ts">
defineProps<{
  number: number | string | null
}>()
</script>

<template>
  <div class="queue-number">
    {{ number ?? '-' }}
  </div>
</template>

<style scoped>
.queue-number {
  font-size: 56px;

  font-weight: bold;

  text-align: center;
}
</style>
