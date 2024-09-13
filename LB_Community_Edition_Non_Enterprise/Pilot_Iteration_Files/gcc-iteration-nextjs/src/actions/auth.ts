'use server'
import { cookies } from 'next/headers'
import { z } from 'zod'
import { redirect } from 'next/navigation'

import { signin, signup } from '@/service/drizzle/utilities/user'
import { COOKIE_NAME } from '@/utility/constants'

const authSchema = z.object({
  email: z.string().email(),
  password: z.string(),
})

export const registerUser = async (prevState: any, formData: FormData) => {
  const data = authSchema.parse({
    email: formData.get('email'),
    password: formData.get('password'),
  })

  try {
    const { token } = await signup(data)
    cookies().set(COOKIE_NAME, token)
  } catch (e) {
    // eslint-disable-next-line no-console
    console.error(e)
    return { message: 'Failed to sign you up' }
  }
  redirect('/dashboard')
}

export const signinUser = async (prevState: any, formData: FormData) => {
  const data = authSchema.parse({
    email: formData.get('email'),
    password: formData.get('password'),
  })

  try {
    const { token } = await signin(data)
    cookies().set(COOKIE_NAME, token)
  } catch (e) {
    // eslint-disable-next-line no-console
    console.error(e)
    return { message: 'Failed to sign you in' }
  }
  redirect('/dashboard')
}
