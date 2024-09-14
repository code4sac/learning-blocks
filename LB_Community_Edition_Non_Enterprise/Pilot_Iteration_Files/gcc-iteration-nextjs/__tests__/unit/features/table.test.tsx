import { describe, expect, test } from 'vitest'
import { render } from '@testing-library/react'
import Table01 from '@/components/ui/table/Table01'
import mockData from '../../mock/exampleTableData.json'

describe('General Table Tests', {}, async () => {
  test('Dashboard manager.', () => {
    const { getByTestId } = render(<Table01 data={mockData} />)

    expect(getByTestId('table_body_01').children.length).toBe(2)
  })
})
