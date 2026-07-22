<template>
  <div class="card">
    <slot />
  </div>
</template>

<style scoped>
.card {
  background: white;

  border-radius: var(--radius);

  padding: 28px;

  border: 1px solid var(--border);

  display: flex;

  flex-direction: column;

  gap: 20px;
}
</style>
