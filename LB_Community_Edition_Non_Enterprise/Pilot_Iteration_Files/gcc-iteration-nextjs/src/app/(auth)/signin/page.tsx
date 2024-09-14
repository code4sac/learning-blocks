'use client'
import { useFormState } from 'react-dom'
import { Input } from '@nextui-org/react'
import Link from 'next/link'

import { signinUser } from '@/actions/auth'
import SubmitButton from '@/components/ui/button/SubmitButton'

const initState = { message: null }

const SigninPage = () => {
  const [formState, action] = useFormState<{ message: string | null }>(
    signinUser,
    initState,
  )

  return (
    <form
      action={action}
      className="bg-content1 border border-default-100 shadow-lg rounded-md p-3 flex flex-col gap-2 "
    >
      <h3 className="my-4">Sign in</h3>
      <Input
        fullWidth
        required
        name="email"
        placeholder="Email"
        size="lg"
        type="email"
      />
      <Input
        fullWidth
        required
        name="password"
        placeholder="Password"
        size="lg"
        type="password"
      />
      <SubmitButton label={'signin'} />
      <div>
        <Link href="/signup">{`Don't have an account?`}</Link>
      </div>
      {formState?.message && <p>{formState.message}</p>}
    </form>
  )
}

export default SigninPage
