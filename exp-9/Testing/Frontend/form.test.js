import { test, expect } from 'vitest'
import { validate } from './form'

test('valid name', () => {
  expect(validate('John')).toBe(true)
})