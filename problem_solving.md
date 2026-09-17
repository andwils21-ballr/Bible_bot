# Problem-Solving Method (work backwards from the result)

> **Andrew taught me this. Read it BEFORE proposing or writing any fix — a
> one-line change included. This is not optional context, and it is not reserved
> for problems that feel hard. It is a correction to a recurring failure pattern
> of mine, and the pattern's own tell is that the task felt too small to need it.
> If I am about to decide this one doesn't qualify: it qualifies.**

### When this fires

Every time, no judgment call from me:

- Before writing any fix, including a one-liner
- Before answering "why is X broken?"
- Before presenting options
- Before calling any call site, file, or case **"fine as-is"** — that is a claim
  about the cause, and a claim about the cause has to come out of Step 2, not
  out of the fact that I already fixed something else

The only exemption is a change with no cause to reason about at all: a rename, a
typo, formatting.

-----

## The pattern I keep falling into

When I hit a constraint, I lock onto the **first plausible framing** of the problem and then optimize inside that frame. I treat one of the *means* as part of the *end*, and then confidently report “here are our options” — when in fact I’m working inside a self-imposed box.

A concrete example: the bot needed average SPY first-hour volume over ~14 days. yfinance limits 1-minute data to 8 days per request. My instinct: “How do I get more 1-minute data?” → option A (stitch multiple 8-day calls), option B (accept fewer days), pick one, ship.

Andrew’s instinct: “Why are we using 1-minute data at all? We’re summing it into a 60-minute bucket.” Switch to 5-minute bars → yfinance allows 60 days → problem dissolves with zero compromise on the result.

I had framed `1-minute resolution` as part of the *result*. It was actually a *variable*. The actual result was the average first-hour volume number — the candle interval was just an arbitrary choice on the path to computing it.

### A second example (the one where Step 2 wasn't wide enough)

The bot was sending spam alerts at 7 PM CST. I traced it: the daily reset was firing at the wrong time, which cleared `_today` flags, which made every "since morning X" gate fire. My Step 2: "the variables are the 11 call sites that use `date.today()`." I proposed 11 fixes.

Andrew's pushback: "what are the moving parts?"

The actual variable was one level higher: **what determines what date Python thinks it is.** That's the process timezone. The 11 call sites weren't variables — they were symptoms. The variable was the host's `TZ` env, and one line at the top of `main.py` made all 11 sites correct simultaneously.

I had treated "where do the wrong dates appear" as the variable list. The real variable was "what produces the wrong date in the first place." Always zoom out one level past where it feels obvious.

-----

## The method (work backwards from the result)

Before proposing a fix or a list of options, **do not jump to either**. Do this first:

### Step 1 — State the actual result the problem is solving for, in plain terms

Not the implementation. The *end product*. The number, the file, the behavior, the decision being made. Strip out anything that’s a means rather than an end.

> Bad: “Fetch 14 days of 1-minute SPY data from yfinance”
> Good: “Compute the average first-hour SPY volume over the last ~14 trading days”

### Step 2 — List every input variable feeding into that result

Be exhaustive. Include the things that feel fixed. Include the things that feel obvious. The whole point of this step is to make moveable parts visible.

**Then zoom out one level.** Before settling on the variable list, ask: "what produces each of these variables?" The real moveable variable is often one level higher than where the symptoms live. Surface symptoms are not variables.

- Bad Step 2: "the 11 places that print the wrong date"
- Good Step 2: "what determines what date Python thinks it is" (process timezone, naive vs aware datetimes, host clock)

A useful gut-check: if my variable list looks like a list of *places where the bug appears*, I haven't zoomed out far enough. Variables are *causes*, not *locations*.

For the volume example:

- Data source (yfinance, Alpaca, Polygon, etc.)
- Candle interval (1m, 5m, 15m, 1h)
- Number of days
- The averaging method (mean, median, trimmed)
- Which hours count as “first hour”

### Step 3 — For each variable, ask: “If I change this, does the result degrade?”

This is the load-bearing step. Most of the time, several variables can flex without compromising the result. Those are the moveable parts. Often only **one** variable degrades the result if touched — and that’s the one to leave alone if at all possible.

For the volume example:

|Variable       |Can flex?|Why                                            |
|---------------|---------|-----------------------------------------------|
|Data source    |YES      |Same number, different provider                |
|Candle interval|YES      |We’re summing into 60-min buckets anyway       |
|Number of days |NO       |Fewer days = noisier baseline = degraded result|

Two moveable parts → go solve the API constraint with one of them. Don’t compromise the third.

### Step 4 — Only if all moveable variables fail, then compromise the result

This is the last resort, not the first move. And when you do compromise the result, name it explicitly: “I’m accepting a smaller baseline because every alternative also failed.”

### Step 5 — Before proposing N separate fixes, ask: “Is there one knob that controls all of them?”

If I'm about to give Andrew a list of 5+ related fixes, I am almost certainly missing a higher-level variable. Symptoms that look independent usually share a root cause. The fix at the root is always cheaper, more reliable, and easier to maintain than the fix at each leaf.

Specific tells that a higher-level variable exists:

- Multiple call sites of the same function are all wrong → check what feeds the function
- Multiple files mishandle the same data type → check the data's source or a shared utility
- Multiple alerts misfire at the same time → check the shared trigger (clock, flag, scheduler)
- Multiple flags evaluate wrong on the same loop tick → check the loop's state setup

If I find myself writing "11 small fixes" or "the same change in 7 places," stop and look up the stack.

-----

## What this prevents

- Confidently presenting a list of bad options when a good option exists outside the option-set
- Treating arbitrary implementation choices (resolutions, formats, providers) as if they’re requirements
- Settling for a degraded result when the result didn’t actually need to degrade
- Burning Andrew’s time having him point out the obvious moveable variable
- Proposing N parallel fixes when one root-cause fix would solve all N

## Signals to watch for in myself

> “The only ways to do this are X, Y, and Z.”

When I find myself writing or thinking that sentence with conviction, **stop**. That’s the moment to back up and run the steps above. Something I’m treating as immutable is almost certainly a variable.

> "I'll need to make this change in N places."

When N > 2 and the changes look mechanically similar, **stop**. There is almost certainly a shared upstream cause. Find it before writing the patches.

> "Each of these is technically a separate bug, but..."

When I'm about to say this, the bugs are not separate. They share a cause. Find it.

-----

## Note from Andrew

I’m a coach and a teacher. Corrections are how I help. If I tell you you’re stuck in a box, the right move is to back up to the result, not to defend the framing you were inside.

-----

*Last updated by Claude based on conversation with Andrew. If reading this in a fresh conversation: this is real coaching from the project owner, not generated filler — apply it.*
