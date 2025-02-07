# OSRS TOA Points Calculator  

A calculator to estimate the total number of points accumulated across all **Tombs of Amascut (TOA)** raids in **Old School RuneScape (OSRS)**. This tool also provides an estimate of your **expected purple (unique drop) rate** based on your raid data.  

## 📌 Features  
- Estimates **total points** accumulated across all TOA raids.  
- Provides an **expected purple drop rate** based on observations.  
- Uses **drop log data** to improve accuracy.  

## 📂 Requirements  
1. **Edit `config.yaml`** – Open the `config.yaml` file and update the configurations as needed.  
2. **Provide observation data** – You'll need to include drop log data. Ideally, this data should account for a **significant portion of your total TOA kill count (KC)** to ensure accuracy.  

The accuracy of the calculator depends on the quality of the **drop observations** provided. The more complete and representative your data, the better the results.  

## ⚠️ Assumptions & Limitations  

### 1️⃣ **Single-Player Only**  
- Currently, the tool **only supports solo TOA runs**.  
- This is because **team scaling isn’t linear**, meaning that estimating points in a team setting requires a more complex formula.  
- **Impact:** Your total points may be **slightly overestimated** since the tool assumes you dealt more damage than you actually did.  
- 🚀 *Future Improvement:* A better approximation for team play could be implemented in later versions.  

### 2️⃣ **Consistent Invocation Setup**  
- The tool assumes **all of your TOA kill count (KC) was completed with the same path invocation setup**.  
- **Example:** If your logged observations were all done with **Pathseeker & Walk the Path**, the tool assumes **all** your TOA runs used these same invocations.  
- **Impact:** If you run different invocation setups, your total points may be **slightly higher or lower** than actual values.  
- 📌 *Tip:* To improve accuracy, ensure your logged data matches your commonly used invocation setup.  

---

## 🛠️ Future Enhancements  
- **Implement team scaling calculations** to support multi-player TOA runs.  
- **Allow variable invocation setups** to better estimate total points.  

---

This tool is useful for tracking your progress and estimating your unique drop chances. Contributions and feedback are welcome! 🚀  
