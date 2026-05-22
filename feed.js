const API_URL = "http://127.0.0.1:8000";

/* =========================
   LOAD RECOMMENDED BLOGS
========================= */

async function loadRecommendedBlogs() {

    try {

        const username = localStorage.getItem("username");

        const response = await fetch(
            `${API_URL}/recommend/${username}`
        );

        const blogs = await response.json();

        console.log("RECOMMENDED BLOGS:", blogs);

        renderBlogs(blogs);

    } catch (error) {

        console.error("LOAD ERROR:", error);

        alert("❌ Failed to load recommended blogs");
    }
}

/* =========================
   RENDER BLOGS
========================= */

function renderBlogs(blogs) {

    const container = document.getElementById(
        "blog-container"
    );

    if (!container) {
        console.error("blog-container not found");
        return;
    }

    container.innerHTML = "";

    if (!Array.isArray(blogs) || blogs.length === 0) {

        container.innerHTML = `

            <div style="
                color:white;
                font-size:22px;
                padding:40px;
            ">
                ❌ No Blogs Found
            </div>

        `;

        return;
    }

    blogs.forEach(blog => {

        container.innerHTML += `

            <div class="blog-card">

                <div class="blog-image">
                    🚀
                </div>

                <div class="blog-content">

                    <div class="category">
                        ${blog.category || "Technology"}
                    </div>

                    <div class="blog-title">
                        ${blog.title || "No Title"}
                    </div>

                    <div class="blog-text">
                        ${(blog.content || "No Content").substring(0,250)}...
                    </div>

                    <div class="actions">

                        <button class="like-btn"
                            onclick="likeBlog(${blog.id})">
                            ❤️ Like
                        </button>

                        <button class="save-btn"
                            onclick="saveBlog(${blog.id})">
                            🔖 Save
                        </button>

                        <button class="read-btn"
                            onclick="trackReading(${blog.id}, '${blog.category}')">
                            📖 Read
                        </button>

                        <button class="recommend-btn"
                            onclick="showRecommendations(${blog.id})">
                            🤖 Recommend
                        </button>

                    </div>

                </div>

            </div>

        `;
    });
}

/* =========================
   SEARCH BLOGS
========================= */

async function searchBlogs() {

    try {

        const query = document.getElementById(
            "search-input"
        ).value.trim();

        if (!query) {

            alert("⚠️ Please enter search text");
            return;
        }

        const response = await fetch(
            `${API_URL}/search/${query}`
        );

        const blogs = await response.json();

        console.log("SEARCH RESULTS:", blogs);

        renderBlogs(blogs);

    } catch(error) {

        console.error("SEARCH ERROR:", error);

        alert("❌ Search Failed");
    }
}

/* =========================
   LIKE BLOG
========================= */

async function likeBlog(blogId) {

    try {

        const username = localStorage.getItem("username");

        await fetch(
            `${API_URL}/like-blog?username=${username}&blog_id=${blogId}`,
            {
                method: "POST"
            }
        );

        alert("✅ Blog Liked!");

    } catch(error) {

        console.log(error);

        alert("❌ Like Failed");
    }
}

/* =========================
   SAVE BLOG
========================= */

async function saveBlog(blogId) {

    try {

        const username = localStorage.getItem("username");

        await fetch(
            `${API_URL}/save-blog?username=${username}&blog_id=${blogId}`,
            {
                method: "POST"
            }
        );

        alert("✅ Blog Saved!");

    } catch(error) {

        console.log(error);

        alert("❌ Save Failed");
    }
}

/* =========================
   TRACK READING
========================= */

async function trackReading(blogId, category) {

    try {

        const username = localStorage.getItem("username");

        await fetch(
            `${API_URL}/track-interaction?username=${username}&blog_id=${blogId}&category=${category}&time_spent=10`,
            {
                method: "POST"
            }
        );

        alert("📖 Reading Tracked!");

    } catch(error) {

        console.log(error);

        alert("❌ Tracking Failed");
    }
}

/* =========================
   SHOW RECOMMENDATIONS
========================= */

async function showRecommendations(blogId) {

    try {

        const response = await fetch(
            `${API_URL}/similar-blogs/${blogId}`
        );

        const recommendations = await response.json();

        console.log("RECOMMENDATIONS:", recommendations);

        const section = document.getElementById(
            "recommendation-section"
        );

        section.innerHTML = `

            <h2 class="section-title">
                🤖 AI Recommendations
            </h2>

        `;

        recommendations.forEach(blog => {

            section.innerHTML += `

                <div class="blog-card"
                     style="margin-bottom:25px;">

                    <div class="blog-content">

                        <div class="category">
                            ${blog.category}
                        </div>

                        <div class="blog-title">
                            ${blog.title}
                        </div>

                        <div class="blog-text">
                            ${blog.content.substring(0,200)}...
                        </div>

                    </div>

                </div>

            `;
        });

    } catch(error) {

        console.log(error);

        alert("❌ Recommendation Failed");
    }
}

/* =========================
   TRENDING BLOGS
========================= */

async function loadTrendingBlogs() {

    try {

        const response = await fetch(
            `${API_URL}/blogs`
        );

        const blogs = await response.json();

        renderBlogs(blogs);

    } catch(error) {

        console.log(error);

        alert("❌ Trending Blogs Failed");
    }
}

/* =========================
   CATEGORIES
========================= */

async function loadCategories() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/all-blogs"
        );

        const blogs = await response.json();

        const container = document.getElementById(
            "blog-container"
        );

        container.innerHTML = "";

        blogs.forEach(blog => {

            container.innerHTML += `

                <div class="blog-card">

                    <div class="blog-image">
                        📚
                    </div>

                    <div class="blog-content">

                        <div class="category">
                            ${blog.category}
                        </div>

                        <div class="blog-title">
                            ${blog.title}
                        </div>

                        <div class="blog-text">
                            ${blog.content.substring(0,250)}...
                        </div>

                        <div class="actions">

                            <button class="like-btn"
                                onclick="likeBlog(${blog.id})">
                                ❤️ Like
                            </button>

                            <button class="save-btn"
                                onclick="saveBlog(${blog.id})">
                                🔖 Save
                            </button>

                            <button class="read-btn"
                                onclick="trackReading(${blog.id}, '${blog.category}')">
                                📖 Read
                            </button>

                            <button class="recommend-btn"
                                onclick="showRecommendations(${blog.id})">
                                🤖 Recommend
                            </button>

                        </div>

                    </div>

                </div>

            `;
        });

    } catch(error) {

        console.log("CATEGORY ERROR:", error);

        alert("❌ Failed to load categories");
    }
}
/* =========================
   SAVED BLOGS
========================= */

function loadSavedBlogs() {

    alert(
        "❤️ Saved Blogs Feature Working"
    );
}

/* =========================
   ANALYTICS
========================= */

function showAnalytics() {

    alert(
        "📈 Analytics Feature Working"
    );
}

/* =========================
   SETTINGS
========================= */

function showSettings() {

    alert(
        "⚙️ Settings Feature Working"
    );
}

/* =========================
   LOGOUT
========================= */

function logoutUser() {

    localStorage.removeItem("username");

    window.location.href = "login.html";
}

/* =========================
   GLOBAL FUNCTIONS
========================= */

window.searchBlogs = searchBlogs;
window.likeBlog = likeBlog;
window.saveBlog = saveBlog;
window.trackReading = trackReading;
window.showRecommendations = showRecommendations;
window.loadTrendingBlogs = loadTrendingBlogs;
window.loadCategories = loadCategories;
window.loadSavedBlogs = loadSavedBlogs;
window.showAnalytics = showAnalytics;
window.showSettings = showSettings;
window.logoutUser = logoutUser;
window.loadRecommendedBlogs = loadRecommendedBlogs;

/* =========================
   AUTO LOAD
========================= */

document.addEventListener(
    "DOMContentLoaded",
    loadRecommendedBlogs
);