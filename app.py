import streamlit as st
import time

# 1. Cấu hình trang
st.set_page_config(page_title="Cat Magic Academy Tycoon", page_icon="🐱", layout="centered")

# 2. Khởi tạo trạng thái game (Session State)
if "gold" not in st.session_state:
    st.session_state.gold = 100
if "cats" not in st.session_state:
    st.session_state.cats = 1
if "school_level" not in st.session_state:
    st.session_state.school_level = 1

# 3. Tiêu đề game
st.title("🧙‍♂️ Cat Magic Academy Tycoon")
st.caption("Game quản lý trường học phép thuật của mèo trên Streamlit!")

# 4. Hiển thị chỉ số
col1, col2, col3 = st.columns(3)
col1.metric("💰 Tiền Vàng", f"{st.session_state.gold} G")
col2.metric("🐱 Học sinh Mèo", f"{st.session_state.cats} con")
col3.metric("🏰 Cấp Trường", f"Cấp {st.session_state.school_level}")

st.divider()

# 5. Khu vực hình ảnh minh họa (Thay URL bằng GIF mèo của bạn)
st.subheader("🏫 Lớp Học Phép Thuật")
st.image(
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1eXp2ZnR4bmRzc292eXFud2x4OW8zeGNuOW14a3BxODR4c2VnZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mCRJDo24UvJMA/giphy.gif",
    caption="Các bé mèo đang luyện tập chế tạo dược phẩm!",
    use_container_width=True
)

st.divider()

# 6. Bảng hành động & Nâng cấp
st.subheader("🛠️ Quản Lý & Nâng Cấp")

col_act1, col_act2 = st.columns(2)

with col_act1:
    if st.button("✨ Thu hoạch Phép thuật (+10 Vàng)"):
        st.session_state.gold += 10 * st.session_state.cats
        st.success("Đã thu hoạch phép thuật!")
        st.rerun()

with col_act2:
    cost_cat = st.session_state.cats * 50
    if st.button(f"🐾 Nhận thêm Mèo mới ({cost_cat} Vàng)"):
        if st.session_state.gold >= cost_cat:
            st.session_state.gold -= cost_cat
            st.session_state.cats += 1
            st.success("Một chú mèo phép thuật mới đã nhập học!")
            st.rerun()
        else:
            st.error("Không đủ vàng!")

cost_level = st.session_state.school_level * 200
if st.button(f"🏰 Nâng Cấp Trường Học ({cost_level} Vàng)"):
    if st.session_state.gold >= cost_level:
        st.session_state.gold -= cost_level
        st.session_state.school_level += 1
        st.success("Trường học đã mở rộng thêm không gian mới!")
        st.rerun()
    else:
        st.error("Chưa đủ tiền nâng cấp!")
      
