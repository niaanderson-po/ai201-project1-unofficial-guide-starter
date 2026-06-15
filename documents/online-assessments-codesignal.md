### CodeSignal

<blockquote>
<b>Changes for spring 2023</b>

Historically, the CodeSignal GCA worked on a 300-850 score scale. Since spring 2023, CodeSignal has transitioned into a newer 200-600 scale that is meant to allow for a common scale with CodeSignal's other tests. See [this](https://github.com/Leader-board/OA-and-Interviews/tree/ce5d21cc90a5c29db768197da8ee2513bbf6f580) if you're looking for the old scale details. Key notes:

* the test content has not changed at all. 
* unlike before, partially correct questions (i.e, from a TLE in Q4 that's common with brute-force solutions) are marked with relative generosity. It used to be the case that you would get almost nothing from a question that you didn't answer perfectly; this is no longer the case. 
* while CodeSignal provides a conversion table from the 300-850 scale to the 200-600 scale, our observation is that it's too simplified. In other words, you cannot use this as a like-for-like conversion between old and new scales, since the parameters used between the two scales have changed (in particular, due to the partial marking changes). See [this](https://www.reddit.com/r/csMajors/comments/1444fg3/codesignal_2023_scores_seems_to_be_glitched/) for more examples. The consequence of this is that a (say) 779 in the old scale could be a 550 or a 520 (and vice-versa), meaning that you'll have to check your new score to see if it's where you want it to be. 

Relevant CodeSignal articles:

* [Understanding Coding Score 2023](https://support.codesignal.com/hc/en-us/articles/13261190299287-Understanding-Coding-Score-2023) - provides a high-level overview of the changes
* [Converting Historical Coding Score Thresholds to Coding Score 2023
  ](https://support.codesignal.com/hc/en-us/articles/13260678794775) - provides a crude conversion table for converting from current scoring scales from all of CodeSignal's tests to the new 200-600 system.

</blockquote>

Normally used by companies for their GCA (General Coding Assessment)
test, which is a standardised coding examination (think of it as the
SAT/ACT of coding for those in the US). As a result,

  - It is possible to submit a test result to multiple companies. This
    goes both ways – if you do well once, you won’t have to retake the
    test for a good period of time as you can simply share the result
    for other companies. Similarly, if you do poorly and several
    companies request that score (and you do not have a better one to
    share), you can run into trouble.

  - This is usually the most proctored test you will need to take. Most
    companies will request the proctored variant of the GCA, which means
    that you will be forced to share your screen, present a form of
    identification before the test and have them record you (though they
    say that companies will not be provided proctoring data and is only
    used to confirm that you didn't cheat). A minority will be fine with
    the unproctored variant, but it is recommended to opt in to
    proctoring since an unproctored test result cannot be sent to
    companies that require proctoring.
  
The nature of the GCA means that there is significantly more uniformity
in the questions you’ll get compared to the other test types. For the
70-minute test, you’ll get 4 questions.

  - Q1 and Q2 are gimmes and should be crushed as soon as possible.

  - Q3 is usually an implementation-heavy LeetCode Medium problem and
    from experience is usually a 2-D matrix problem that is very *bashing*-friendly. What this means is
    there isn’t much in the way of algorithmic complexities to bother
    with – the solution is long, but you simply need to do what it asks
    you to do without worrying about time complexity and such.
    <details>
    <summary>LeetCode questions that approximate a CodeSignal Q3</summary>
    
    * https://leetcode.com/problems/spiral-matrix/
    * https://leetcode.com/problems/spiral-matrix-ii/
    * https://leetcode.com/problems/rotate-image/
    * https://leetcode.com/problems/diagonal-traverse/
    * https://leetcode.com/problems/reshape-the-matrix/
    * https://leetcode.com/problems/toeplitz-matrix/
    * https://leetcode.com/problems/image-overlap/
    * https://leetcode.com/problems/largest-local-values-in-a-matrix/
    * https://leetcode.com/problems/transpose-matrix/
    * https://leetcode.com/problems/count-square-submatrices-with-all-ones
    * https://leetcode.com/problems/sort-matrix-by-diagonals
    * https://leetcode.com/problems/text-justification - this is on the harder side but is a good example of a string-based implementation problem for Q3
    
    Aim to get them in 15-20 minutes or so. 
    </details>

  - Q4 is a purely algorithmic LeetCode Medium problem – here you will
    need to focus on making sure that the time complexity is optimal. From
    experience Q4 normally involves a clever application of hashmaps and
    it is expected that you know how to work with it properly inside and out. While
    greedy problems are technically possible, DP (dynamic programming)
    questions will *not* show up in Q4 (and this test). 

    <details>
    <summary>LeetCode questions that approximate a CodeSignal Q4</summary>

      * https://leetcode.com/problems/longest-consecutive-sequence/
      * https://leetcode.com/problems/4sum-ii/ (note: it's unlikely that a CodeSignal Q4 will ask for an O(_n_<sup>3</sup>) solution as optimal, but this is still good practice)
      * https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
      * https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
      * https://leetcode.com/problems/array-of-doubled-pairs/
      * https://leetcode.com/problems/3sum-with-multiplicity/
      * https://leetcode.com/problems/count-number-of-nice-subarrays/
      * https://leetcode.com/problems/k-diff-pairs-in-an-array/
      * https://leetcode.com/problems/diagonal-traverse-ii/
      * https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/description/
      * https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/
      * https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits
      * https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs

  
    Aim to get them in 20-30 minutes or so.
    </details>

It is a very good idea to read CodeSignal's [coding assessment framework](./media/general-coding-assessment-framework.pdf). That document tells what would (and not) be tested on the GCA, and clearly tells that DP isn't on the test for instance. You can also get a couple of extra practice questions by going [here](./media/General-Coding-Skills-Evaluation-Framework-CodeSignal-Skills-Evaluation-Lab-Short.pdf).

Now what about scores? The scoring range is 200 to 600, and the more you get, the better. Completing all four questions of the test perfectly will get you a 600.

#### Retaking tests

CodeSignal historically had a generous retaking policy - one could resit the exam every two weeks. This means that the "damage" in case of a bad score was considerably limited, as you could normally just resit. 

This has changed since 2023: only two tests can be taken in a rolling 30-day period, and only three tests can be taken in a rolling 6-month period. This means that there is a much higher chance that you'll have no retakes, and means that you'll have to be more careful. See [this page](https://support.codesignal.com/hc/en-us/articles/11635510785047-What-is-a-cooldown-period-and-how-does-it-impact-my-ability-to-take-an-assessment-) for more information.

The only exception to this rule are cases where you won't have a valid result, such as if a company asks for a test that has been taken in (say) the last two months and you don't have such a result. 

#### How long are my results valid for?

Your test results are technically valid without an expiration date. However, companies have the right to set a limit on how old a test result must be, as described at [here](https://support.codesignal.com/hc/en-us/articles/1500001964122--Setting-age-limits-for-certification-results). What this means is that if you have a company that wants, for instance, only results in the last 6 months, but your latest result was earlier than that, you will not have a choice but to retake the exam, and a similar issue can happen if you had an older result that was better than a "valid" test result. Of course, those results will still be valid for those companies that don't use this feature, and you retain the right to retake the test even if you do have a valid result that meets this age limit. 

![A CodeSignal test report (which is similar to what companies will
see)](./media/image10.png)

**Figure 3**: A CodeSignal test report (which is similar to what companies will
see)

Notice above that you’ll get a square graph that show
your implementation, problem-solving and speed – do not worry about them
too much. The scaled score out of 600 is the most important. Also, complete as much of the test as you can. It is better to write a brute-force solution for Q4 and get half points than to leave it blank - since spring 2023, CodeSignal has been more generous in marking partial solutions (they used to be very stingy with non-perfect solutions in the past).  

It may help to try out some CodeSignal GCA practice tests (which you can
take every day or so). The questions give a good approximation on what you would get on the actual
test.

In rare cases (such as SIG), you may be given a non-GCA examination (wherein the
questions are written by the company, much like HackerRank, and there is
no scaled score), in which case most of what was written for the HackerRank section would
apply instead. It's easy to find out if an exam is GCA - this will be clearly mentioned. 

Note that this guide does not cover tests such as CodeSignal's Data Science and Industry Coding frameworks (though there is a [nice guide](https://github.com/PaulLockett/CodeSignal_Practice_Industry_Coding_Framework) for the latter). 
