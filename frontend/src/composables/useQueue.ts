import { computed } from 'vue'

import { storeToRefs } from 'pinia'

import { useQueueStore } from '@/stores/queue'

export function useQueue() {
  const store = useQueueStore()

  const { queue, loading, myQueue } = storeToRefs(store)

  const currentQueue = computed(() => queue.value?.current_queue ?? '-')

  const lastQueue = computed(() => queue.value?.last_queue ?? '-')

  const remaining = computed(() => queue.value?.remaining ?? '-')

  return {
    queue,

    loading,

    myQueue,

    currentQueue,

    lastQueue,

    remaining,

    fetchQueue: store.fetchQueue,

    takeQueue: store.takeQueue,

    setQueue: store.setQueue,
  }
}
