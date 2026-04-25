# 66. Plus One

**Easy**

## 🧩 Problem

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the *i-th digit* of the integer. The digits are ordered from most significant to least significant, and the integer does not contain any leading zeros.

Increment the integer by one and return the resulting array of digits.

---

## 📥 Examples

### Example 1:

```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
```

### Example 2:

```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
```

### Example 3:

```
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
```

---

## 📌 Constraints

* `1 <= digits.length <= 100`
* `0 <= digits[i] <= 9`
* `digits` does not contain leading zeros

---

## 💡 Approach

We simulate how addition works manually:

* Start from the last digit
* Add `1`
* If the result is `10`, set it to `0` and carry over
* Continue moving left until no carry remains
* If all digits were `9`, insert `1` at the beginning

---

## ⚡ Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)` (in-place)

---

## 🧠 Follow-up

Can you solve this without converting the array into an integer?
