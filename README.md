# The 12 Coins Problem

## Problem Statement

You have 12 coins, of which 11 are real and one is fake. You know the fake coin has a different weight from the real coins, but you don't know if it is heavy or light. You also have a balance scale that can be used to tell which of two piles of coins is heavier (or if they weigh the same). Can you determine which coin is fake, and whether it is heavy or light, using the the balance scale only three times?

## Chloe's Solution (with some objects renamed to match the python code)

This solution is implemented in `chloes-solution.py`

Divide the 12 coins into three groups of four coins each, and name them as follows:
- Group A: A0, A1, A2, A3
- Group B: B0, B1, B2, B3
- Group C: C0, C1, C2, C3.

**Weighing #1**: Group A vs Group B
- If they weigh the same, go to `Finding one fake among four potential fakes, with four known reals as reference, in two weighings`
- If they weigh differently, `Finding one fake among 4 heavy and 4 light potential fakes, with four known reals as reference, in two weighings`

### Finding one fake among four potential fakes, with four known reals as reference, in two weighings

Since Group A and Group B weighed the same, we know all coins A and B are real, and one of the coins in Group C is fake and could be heavy or light.

**Weighing 2**: [C0, C1, C2] vs [A0, A1, A2]
- If they weigh the same, then C3 is fake. **Weighing #3**: C3 vs any other coin to determine whether C3 is heavy or light.
- If they don't balance, then we know one of C0, C1, or C2 is fake and whether it is heavy or light. **Weighing #3**: C0 vs C1 to determine which coin is fake.

### Finding one fake among 4 heavy and 4 light potential fakes, with four known reals as reference, in two weighings

Without loss of generality, say Group A was heavier than Group B. Then we know all coins C are real, and one coin A is fake and heavy or one coin B is fake and light.*

**Weighing #2**: [A0, B0, B1, B2] vs [B3, C0, C1, C2]
- If they weigh the same, then we removed the fake coin. Since all coins C are real and all coins B were included in this weighing, the fake coin must have been one of A1, A2, or A3, and we know it is heavy. **Weighing #3**: A1 vs A2 to determine which coin is fake.
- If [A0, B0, B1, B2] is heavier than [B3, C0, C1, C2], then either [A0, B0, B1, B2] contains a heavy fake which must be A0, or [B3, C0, C1, C2] contains a light fake which must be B3. **Weighing #3**: A0 vs any coin other than B3 to determine which coin is fake.
- If [A0, B0, B1, B2] is lighter than [B3, C0, C1, C2], then either [A0, B0, B1, B2] contains a light fake coin which must be one of B0, B1, or B2; or [B3, C0, C1, C2] contains a heavy fake coin, which is impossible because all coins C are real and all coins B are real or light. Thus, the fake coin is one of B0, B1, or B2. **Weighing #3**: B0 vs B1 to determine which coin is fake.

## Other solutions

Apparently Maria has a different solution?