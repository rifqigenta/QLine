<script setup lang="ts">
defineProps<{
  text: string
}>()
</script>

<template>
  <div class="empty">
    {{ text }}
  </div>
</template>

<style scoped>
.empty {
  text-align: center;

  color: #94a3b8;

  padding: 24px;
}
</style>
