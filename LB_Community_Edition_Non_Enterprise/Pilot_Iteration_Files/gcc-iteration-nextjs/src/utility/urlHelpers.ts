import { NextRequest, NextResponse } from 'next/server'

function buildUrl() {
  let context = {
    navigationKey: 'example 01',
    queryKey: '1efa02',
  }
  let query = `q=${context.queryKey}&n=${context.navigationKey}`
  return query
}

export function defaultDashboard(request: NextRequest) {
  return NextResponse.redirect(new URL(`dashboard?${buildUrl()}`, request.url))
}
