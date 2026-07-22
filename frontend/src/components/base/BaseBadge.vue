<script setup lang="ts">
defineProps<{
  color?: 'primary' | 'success' | 'danger'
}>()
</script>

<template>
  <span class="badge" :class="color">
    <slot />
  </span>
</template>

<style scoped>
.badge {
  display: inline-flex;

  align-items: center;

  justify-content: center;

  padding: 6px 12px;

  border-radius: 999px;

  font-size: 14px;

  font-weight: 600;
}

.primary {
  background: #ede9fe;

  color: #7c3aed;
}

.success {
  background: #dcfce7;

  color: #16a34a;
}

.danger {
  background: #fee2e2;

  color: #dc2626;
}
</style>
