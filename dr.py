import streamlit as st
from datetime import datetime

# Define conversion categories
conversion_categories = {
    "Baby Weight Estimation": ["Baby Weight Estimation"],
    "Length/Distance": ["Meters to Kilometers", "Miles to Kilometers", "Inches to Centimeters"],
    "Mass/Weight": ["Kilograms to Pounds", "Grams to Ounces"],
    # Add other categories and conversions as needed
}

# Define unit symbols (if needed)
unit_symbols = {
    "Meters": "m",
    "Kilometers": "km",
    "Miles": "mi",
    "Inches": "in",
    "Centimeters": "cm",
    "Kilograms": "kg",
    "Pounds": "lbs",
    "Grams": "g",
    "Ounces": "oz",
    # Add other units as needed
}

# Define conversion functions (add your conversion logic here)
def CONVERSIONS(conversion_type):
    # Example conversion logic (add more conversions as needed)
    def meters_to_kilometers(value):
        return value / 1000
    
    def kilometers_to_miles(value):
        return value * 0.621371
    
    # Example dictionary of conversion functions
    conversion_dict = {
        "Meters to Kilometers": meters_to_kilometers,
        "Kilometers to Miles": kilometers_to_miles,
        # Add other conversions here
    }
    
    return conversion_dict.get(conversion_type)

# Baby weight estimation function (dummy example)
def estimated_baby_weight(mother_weight, gestational_weeks):
    # Simple estimation logic (replace with your own logic)
    return mother_weight * 0.15

def main():
    # Set background color using CSS
    st.markdown(
        """
        <style>
        .reportview-container {
            background-color: #f0f8ff;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Displaying a Baby Image/Icon with a beautiful message
    st.image("baby_image.jpg", width=300)  # Correct direct image URL
    st.markdown(
        "<h1 style='text-align: center;'>Baby & Baba Weight Estimator & More</h1>", unsafe_allow_html=True
    )
    st.markdown(
        "<h3 style='text-align: center;'>Where every little moment matters 💖✨</h3>", unsafe_allow_html=True
    )
    st.markdown(
        "<h4 style='text-align: center;'>Let’s create wonders for the little ones! 🍼👼</h4>", unsafe_allow_html=True
    )

    # Your existing conversion and baby weight estimator logic follows here...
    # Initialize session state
    if 'history' not in st.session_state:
        st.session_state.history = []

    category = st.selectbox("📦 Category", list(conversion_categories.keys()))
    
    conversion_type = st.selectbox(
        "🔄 Conversion Type",
        conversion_categories[category],
        format_func=lambda x: (
            x  # Return as-is if not "X to Y" format
            if ' to ' not in x 
            else f"{x.split(' to ')[0]} ({unit_symbols.get(x.split(' to ')[0], '')}) → {x.split(' to ')[1]} ({unit_symbols.get(x.split(' to ')[1], '')})"
        )
    )

    # Handling Baby Weight Estimation
    result = None
    if category == "👶Baby Weight Estimation":
        col1, col2 = st.columns(2)
        with col1:
            mother_weight = st.number_input("Mother's Weight (kg)", min_value=30.0, max_value=200.0, value=65.0)
        with col2:
            gestational_weeks = st.number_input("Gestational Weeks", min_value=24, max_value=42, value=40)
        
        if st.button("Estimate Baby Weight"):
            result = estimated_baby_weight(mother_weight, gestational_weeks)
    else:
        value = st.number_input(f"📥 Enter {conversion_type.split(' to ')[0]}", min_value=0.0, format="%.4f")
        if st.button("🔁 Convert"):
            if conversion_type in CONVERSIONS:
                result = CONVERSIONS(conversion_type)(value)
            else:
                st.error("Conversion type not supported")

    if result is not None:
        if category == "Baby Weight Estimation":
            st.success(f"Estimated Birth Weight: {result:.2f} kg")
            entry = f"Mother: {mother_weight}kg, Weeks: {gestational_weeks} → Baby: {result:.2f}kg"
        else:
            from_unit, to_unit = conversion_type.split(' to ')
            st.success(f"{value:.2f} {unit_symbols[from_unit]} = {result:.2f} {unit_symbols[to_unit]}")
            entry = f"{value:.2f}{unit_symbols[from_unit]} → {result:.2f}{unit_symbols[to_unit]}"
        
        # Update history
        st.session_state.history = [{
            "entry": entry,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }] + st.session_state.history[:4]

    # History Section
    if st.session_state.history:
        with st.expander("📚 Conversion History (Last 5)"):
            for item in st.session_state.history[:5]:
                st.markdown(f"⏰ {item['timestamp']} - {item['entry']}")

    # Thank You and Created By Section
    st.markdown(
        "<hr>", unsafe_allow_html=True
    )
    st.markdown(
        "<h5 style='text-align: center;'>💖 Created with love by Farida Bano</h5>", unsafe_allow_html=True
    )
    st.markdown(
        "<h6 style='text-align: center;'>✨ Thank you for using the Baby Weight Estimator! ✨</h6>", unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
