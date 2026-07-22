<template>
  <main class="page">
    <slot />
  </main>
</template>

<style scoped>
.page {
  min-height: 100vh;

  display: flex;

  align-items: center;

  justify-content: center;

  background: var(--background);
}
</style>
