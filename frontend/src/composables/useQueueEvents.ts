import { onBeforeUnmount } from 'vue'

interface QueueUpdatedEvent {
  type: string
  shop: string
  current_queue: number | null
  last_queue: number
  remaining: number
  status: string
}

export function useQueueEvents(
  publicCode: string,
  onQueueUpdated: (data: QueueUpdatedEvent) => void,
) {
  const eventSource = new EventSource(`${import.meta.env.VITE_API_URL}/shops/${publicCode}/events`)

  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data)

    if (data.type === 'queue_updated') {
      onQueueUpdated(data)
    }
  }

  eventSource.onerror = () => {
    console.error('SSE disconnected')
  }

  onBeforeUnmount(() => {
    eventSource.close()
  })

  return {
    eventSource,
  }
}
