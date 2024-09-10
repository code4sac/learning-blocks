import { describe, expect, test } from 'vitest'
import { render, screen } from '@testing-library/react'
import LandingPage02 from '@/features/landingPage/LandingPage02'

/**
 * Currently not working. Landing page tests.
 *
 */
describe('Default landing page tests.', {}, () => {
  test('Landing page should container a Live Demo button.', async () => {
    render(<LandingPage02 />)

    expect(screen.getByText('Live Demo')).not.toBeNull()
  })
})
