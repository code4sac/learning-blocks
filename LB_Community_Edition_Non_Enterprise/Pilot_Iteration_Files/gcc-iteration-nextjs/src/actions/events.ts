'use server'

import randomName from '@scaleway/random-name'
import { revalidateTag } from 'next/cache'

import { getCurrentUser } from '@/app/(auth)/users'
import { events } from '@/service/drizzle/schema'
import { db } from '@/utility/db'
import { delay } from '@/utility/delay'

export const createNewEvent = async () => {
  await delay(1000)
  const user = await getCurrentUser()

  await db.insert(events).values({
    startOn: new Date().toUTCString(),
    createdById: user.id,
    isPrivate: false,
    name: randomName('event', ' '),
  })

  revalidateTag('events')
  revalidateTag('dashboard:events')
}
