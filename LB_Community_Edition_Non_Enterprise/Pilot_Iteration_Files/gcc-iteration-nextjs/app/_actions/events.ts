'use server'

import { db } from '@/database/db'
import { events } from '@/database/schema'
import { delay } from '@/app/utilities/delay'
import { getCurrentUser } from '@/app/utilities/users'
import randomName from '@scaleway/random-name'
import { revalidateTag } from 'next/cache'

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
