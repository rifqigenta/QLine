import client from './client'

import type { QueueStatus, TakeQueueResponse } from '@/types/queue'

export async function getQueueStatus(publicCode: string) {
  const response = await client.get(`/shops/${publicCode}/queue`)

  return response.data.data as QueueStatus
}

export async function takeQueue(publicCode: string) {
  const response = await client.post(`/shops/${publicCode}/queue`)

  return response.data.data as TakeQueueResponse
}

export async function nextQueue(publicCode: string) {
  const response = await client.post(`/shops/${publicCode}/queue/next`)

  return response.data.data as QueueStatus
}
