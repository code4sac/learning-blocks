'use server'

import { COOKIE_NAME } from '@/utilities/constants'
import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'

export const signout = () => {
  cookies().delete(COOKIE_NAME)
  redirect('/signin')
}
