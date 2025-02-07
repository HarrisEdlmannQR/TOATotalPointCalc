# OSRS TOA Points Calculator  

A calculator to estimate the total number of points accumulated across all **Tombs of Amascut (TOA)** raids in **Old School RuneScape (OSRS)**. This tool also provides an estimate of your **expected purple (unique drop) rate** based on your raid data.  

## 📌 Features  
- Estimates **total points** accumulated across all TOA raids.  
- Provides an **expected purple drop rate** based on total points.  
- Uses your own **drop log data** as sample data.
  
## 📂 Requirements  
1. **Edit `config.yaml`** – Open the `config.yaml` file and update the configurations as needed.  
2. **Provide observation data** – You'll need to include drop log data. Ideally, this data should account for a **significant proportion of your total TOA kill count (KC)** to ensure accuracy.  

The accuracy of the calculator depends on the quality of the **sample data** provided. The more complete and representative your data, the better the results.  

## 📋 Method

Your sample drop data is compared to simulated drop data for a range of raid levels using the **least sqaures** approach. This means that the raid level that gives the *minimum sum of squared residuals* is the average raid level that provides simulated drops most similar to your sample drops data. Hence, to calculate this simulated data a variety of assumptions are made that may impact the result.

## ⚠️ Assumptions & Limitations  

### 1️⃣ **Only supports solo raids**  
- Currently, the tool **only supports solo TOA runs**.  
- This is because **team scaling isn’t linear**, meaning that estimating points in a team setting requires a more complex formula.  
- **Impact:** If many of your **KC** are in team raids your total points may be **slightly overestimated**.
- 🚀 *Future Improvement:* A better approximation for team play could be implemented since team scaling is known. Allow users to configure a rough estimate of what proportions of their **KC** where completed in team raids between 1 and 8 players.

### 2️⃣ **Single Path Invocation Setup**  
- The tool assumes **all of your TOA kill count (KC) was completed with the same path invocation setup**.  
- **Example:** If you config file indcates **Pathseeker & Walk the Path** invos, the tool assumes **all** your TOA runs used these same invocations.  
- **Impact:** If you run different path invocation setups, your total points may be **slightly higher or lower** than actual values depending on if you ran easier or harder path invos respectively.
- 🚀 *Future Improvment:* Allow users to configure a rough estimate for what proportion of their **KC** was done in certain path invo setups.

### 3️⃣ **Deathless**  
- The tool assumes **all of your TOA kill count (KC) was completed deathless**.   
- **Impact:** Obviously deaths will reduce your points
- 🚀 *Future Improvment:* Allow users to configure a rough estimate for what proportion of their **KC** was done in certain path invo setups.

## 🛠️ Future Enhancements  
- **Implement team scaling calculations** to support multi-player TOA runs.  
- **Allow variable invocation setups** to better estimate total points.  

---

This tool is useful for tracking your progress and estimating your unique drop chances. Contributions and feedback are welcome! 🚀  
