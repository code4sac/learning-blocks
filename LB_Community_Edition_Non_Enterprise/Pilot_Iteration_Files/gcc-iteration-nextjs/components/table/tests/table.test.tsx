import {describe, expect, it, test} from 'vitest';
import {render} from "@testing-library/react";
import mockData from './exampleTableData.json'
import Table01 from "@/components/table/Table01";

test('Test 01', async () => {
  expect(1 + 2).toBe(3)
})

describe('Table', async () => {
  it('should render the the list of movies', () => {
    const {getByTestId} = render(<Table01 data={mockData}/>);
    expect(
      getByTestId('table01').children.length
    ).toBe(1);
  });
})