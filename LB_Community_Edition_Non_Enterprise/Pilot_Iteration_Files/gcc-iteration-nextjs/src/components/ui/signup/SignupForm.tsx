'use client'

import { useFormState } from 'react-dom'
import { Input } from '@nextui-org/react'
import Link from 'next/link'

import { registerUser } from '@/actions/auth'

import Submit from './Submit'

const initState = { message: null }

const SignupForm = () => {
  const [formState, action] = useFormState<{ message: string | null }>(
    registerUser,
    initState,
  )

  return (
    <form
      action={action}
      className="bg-content1 border border-default-100 shadow-lg rounded-md p-3 flex flex-col gap-2 "
    >
      <h3 className="my-4">Sign up</h3>
      <Input fullWidth required name="email" placeholder="Email" size="lg" />
      <Input
        fullWidth
        required
        name="password"
        placeholder="Password"
        size="lg"
        type="password"
      />
      <Submit label={'signup'} />
      <div>
        <Link href="/signin">{`Already have an account?`}</Link>
      </div>
      {formState?.message && <p>{formState.message}</p>}
    </form>
  )
}

export default SignupForm
