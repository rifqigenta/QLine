export interface QueueStatus {
  current_queue: number | null

  last_queue: number

  remaining: number

  status?: string
}

export interface TakeQueueResponse {
  queue_number: number

  status: string

  queue_date: string
}
