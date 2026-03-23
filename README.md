# Anime Discovery & Recommendation Engine

## 🚀 Overview
This project is a full-stack data science application that provides personalized anime recommendations by processing a sparse **15GB user-interaction dataset**. Transitioning from high-level research in Jupyter Notebooks to a functional web dashboard, the system identifies deep latent relationships between 13,000+ titles that traditional genre-tagging often misses.

🎥 **Watch the Full-Stack Demo on YouTube:** [Click Here to Watch](https://youtu.be/qJT_vZLe0Go)

![Anime Recommendation App Workflow](./demo/anime_app_workflow.png)

---

## 🕹️ How to Run Locally
To explore the interactive recommendation dashboard on your own machine, follow these steps:

1. **Prerequisites:** Ensure you have **Python 3.10+** installed on your system.
2. **Clone** this repository to your local machine.
3. **Download the Data Matrix:** Due to GitHub's file size limits, the pre-computed 1GB similarity matrix is hosted externally. Download `training_vals.npy` from **[this Google Drive link](https://drive.google.com/file/d/1J3NRn_sCGQh2axZoI2CyPrgov1W1I5s4/view?usp=sharing)**.
4. **Place the File:** Move the downloaded `training_vals.npy` file directly into the `/app` folder of your cloned repository.
5. **Launch:** Double-click **`run_website.bat`** inside the `/app` folder.
   * *This script automatically handles virtual environment creation, dependency installation (`Flask`, `pandas`, `numpy`), and launches the web server.*
   * Once running, the dashboard will instantly open in your browser at `http://127.0.0.1:5000`.

---

## 🛠️ Technical Implementation

### **1. Core Algorithmic Architecture**
* **Spectral Clustering:** Constructed similarity matrices using cosine similarity of user rating vectors, performing spectral embedding via normalized graph Laplacian eigen decomposition to discover 13 distinct thematic "communities".
* **Recommendation Logic:** Built a user-based collaborative filtering engine using per-item nearest neighbor matching, backed by a **custom Max-Heap (Priority Queue)** to efficiently rank top recommendations in $O(K \log N)$ time.
* **Big Data Optimization:** Managed a sparse 15GB user-rating dataset using **SciPy CSR matrices**, allowing for high-speed similarity calculations and eigendecompositions on consumer hardware.

### **2. Validation & Testing**
* **Mathematical Fidelity:** Developed a custom Fidelity Scoring metric to evaluate data purity, relation preservation, and size balance. 
* **Human-in-the-Loop Validation:** Designed an automated "Odd One Out" quiz using k-medoids selection. Distributed to anime communities, the algorithm's clusters aligned with human perception significantly above random chance (92.3% of questions beat the baseline).

### **3. Advanced Research & Exploration (Multimodal)**
* **Computer Vision:** Engineered experimental pipelines using **ResNet50** and **VGG16** to extract visual embeddings from anime cover art to test aesthetic-based clustering. 
* **Dimensionality Reduction:** Implemented **Singular Value Decomposition (SVD)** to condense image feature complexity while maintaining 90%+ variance during the exploratory phase. *(Note: User rating vectors ultimately proved mathematically superior to image-based clustering for this specific dataset).*

### **4. Full-Stack Web Application**
* **Frontend/Backend:** Architected a **Flask** web dashboard from scratch, featuring real-time client-side search filtering and dynamic recommendation generation.
* **UX:** Designed for simplicity, allowing users to rate their favorite shows and receive instant, personalized suggestions based on nearest-neighbor behaviors.

---

## 📘 Detailed Methodology
For a deep dive into the mathematical foundations, data processing pipeline, and algorithmic validation, please refer to the **[Technical_Report_Anime_Recommendations.pdf](./Technical_Report_Anime_Recommendations.pdf)** located in the root directory.

---

## 👥 Collaboration & Credits
This system was built as a highly collaborative effort. While all three of us contributed to the overarching system design, data strategy, and algorithmic architecture, we each took primary ownership over specific technical domains:

* **Yitschak Kupinsky** ([yitschak.kupinsky@mail.huji.ac.il](mailto:yitschak.kupinsky@mail.huji.ac.il)): Lead Architect of the **Full-Stack Web Application**, independent developer of the exploratory **Multimodal Image Analysis (SVD/ResNet)** pipeline, and developer of the **Max-Heap ranking system**.
* **Osher Serero** ([osher.serero@mail.huji.ac.il](mailto:osher.serero@mail.huji.ac.il)): Primary focus on the **Core Clustering Logic**, similarity matrix optimizations, handling sparse data structures, and statistical data analysis.
* **Ehud Kotegaro** ([ehud.kotegaro@mail.huji.ac.il](mailto:ehud.kotegaro@mail.huji.ac.il)): Primary focus on **Model Validation**, designing the robust Fidelity Testing framework, and engineering the "Odd One Out" human-validation logic and cross-analysis.

---

## 👨‍💻 Primary Contact
**Yitschak Kupinsky**
* [LinkedIn](https://www.linkedin.com/in/yitzchak-kupinsky/)
* yitzchak.kupinsky@gmail.com