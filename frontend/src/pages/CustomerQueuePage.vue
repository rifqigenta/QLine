<script setup lang="ts">
import { onMounted } from 'vue'

import BaseButton from '@/components/base/BaseButton.vue'
import BaseCard from '@/components/base/BaseCard.vue'
import BaseContainer from '@/components/base/BaseContainer.vue'
import BasePage from '@/components/base/BasePage.vue'
import AppHeader from '@/components/layouts/AppHeader.vue'
import QueueInfoCard from '@/components/queue/QueueInfoCard.vue'
import { useQueueEvents } from '@/composables/useQueueEvents'

import { useQueue } from '@/composables/useQueue'

const { currentQueue, lastQueue, remaining, myQueue, loading, fetchQueue, takeQueue, setQueue } =
  useQueue()

const PUBLIC_CODE = 'A7XK29P4'

onMounted(() => {
  fetchQueue(PUBLIC_CODE)
})

useQueueEvents(PUBLIC_CODE, (event) => {
  setQueue({
    current_queue: event.current_queue,
    last_queue: event.last_queue,
    remaining: event.remaining,
    status: event.status,
  })
})

function handleTakeQueue() {
  takeQueue(PUBLIC_CODE)
}
</script>

<template>
  <BasePage>
    <BaseContainer>
      <AppHeader shop-name="René Coffee" />

      <BaseCard>
        <QueueInfoCard title="Sedang Dilayani" :value="currentQueue" />

        <QueueInfoCard title="Sisa Antrean" :value="remaining" />

        <QueueInfoCard title="Antrean Terakhir" :value="lastQueue" />

        <BaseButton :loading="loading" @click="handleTakeQueue"> Ambil Nomor </BaseButton>

        <QueueInfoCard title="Nomor Saya" :value="myQueue ?? '-'" />
      </BaseCard>

      <footer class="footer">Made with ❤️ by René</footer>
    </BaseContainer>
  </BasePage>
</template>

<style scoped>
.footer {
  margin-top: 24px;
  text-align: center;
  font-size: 12px;
  color: var(--text-secondary);
}
</style>
