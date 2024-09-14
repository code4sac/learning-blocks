'use server'

import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'

import { COOKIE_NAME } from '@/utility/constants'

export const signout = () => {
  // eslint-disable-next-line drizzle/enforce-delete-with-where
  cookies().delete(COOKIE_NAME)
  redirect('/signin')
}
