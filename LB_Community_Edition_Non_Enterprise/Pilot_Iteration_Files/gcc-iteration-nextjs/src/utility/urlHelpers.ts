import { NextRequest, NextResponse } from 'next/server'

function buildUrl() {
  let context = {
    navigationKey: 'example 01',
    queryKey: '1efa02',
  }
  let path = 'dashboard'
  let query = `q=${context.queryKey}&n=${context.navigationKey}`
  return new URL(`/${path}?${query}`)
}

export function defaultDashboard(request: NextRequest) {
  return NextResponse.redirect(buildUrl())
}
