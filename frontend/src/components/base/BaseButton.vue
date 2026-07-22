<script setup lang="ts">
defineProps<{
  loading?: boolean
}>()
</script>

<template>
  <button class="button" :disabled="loading">
    <slot />
  </button>
</template>

<style scoped>
.button {
  width: 100%;

  height: 54px;

  border: none;

  border-radius: var(--radius);

  background: var(--primary);

  color: white;

  font-size: 16px;

  font-weight: 600;

  cursor: pointer;

  transition:
    background 0.2s,
    transform 0.2s,
    opacity 0.2s;
}

.button:hover:not(:disabled) {
  background: var(--primary-dark);

  transform: translateY(-1px);
}

.button:active:not(:disabled) {
  transform: translateY(0);
}

.button:disabled {
  opacity: 0.6;

  cursor: not-allowed;
}
</style>
