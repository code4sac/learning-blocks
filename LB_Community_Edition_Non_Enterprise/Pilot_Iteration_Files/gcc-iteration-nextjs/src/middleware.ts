import { NextRequest, NextResponse } from 'next/server'

import { COOKIE_NAME } from '@/utility/constants'

import { defaultDashboard } from './utility/urlHelpers'

export function middleware(request: NextRequest) {
  if (request.nextUrl.pathname.startsWith('/dashboard')) {
    if (!request.cookies.has(COOKIE_NAME)) {
      return NextResponse.redirect(new URL('/signin', request.url))
    }
  }

  if (request.nextUrl.pathname === '/') {
    return defaultDashboard(request)
  }
}

export const config = {
  matcher: ['/dashboard/:path*', '/'],
}
