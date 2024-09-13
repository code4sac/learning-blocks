import 'server-only'
import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'
import { cache } from 'react'

import { getUserFromToken } from '@/service/drizzle/utilities/user'

import { COOKIE_NAME } from '../../utility/constants'

export const getCurrentUser = cache(async () => {
  const token = cookies().get(COOKIE_NAME)
  if (!token) redirect('/signin')

  const user = await getUserFromToken(token)
  if (!user) redirect('/signin')

  return user
})
