import { defineStore } from 'pinia'

import { getQueueStatus, takeQueue } from '@/api/queueApi'

import type { QueueStatus } from '@/types/queue'

export const useQueueStore = defineStore('queue', {
  state: () => ({
    loading: false,

    queue: null as QueueStatus | null,

    myQueue: null as number | null,
  }),

  actions: {
    async fetchQueue(publicCode: string) {
      this.loading = true

      try {
        this.queue = await getQueueStatus(publicCode)
      } finally {
        this.loading = false
      }
    },

    async takeQueue(publicCode: string) {
      const result = await takeQueue(publicCode)

      this.myQueue = result.queue_number

      await this.fetchQueue(publicCode)
    },
  },
})
