import streamlit as st
import plotly.graph_objects as go
from PIL import Image
import base64
from io import BytesIO

# Set page configuration
st.set_page_config(
    page_title="TerraWatt Finance Model",
    page_icon="📊",
    layout="wide"
)

# Define Sankey diagram function
def create_sankey():
    # Define nodes
    labels = [
        # Layer 1 - Production Facility
        "TerraWatt", "Local Partners", "Precast Facility",
        # Layer 2 - Housing REIT
        "Debt Finance", "Equity Finance", "University", "Housing REIT",
        # Final
        "Investors"
    ]

    # Define colors (consistent but distinct per group)
    colors = [
        "#2E91E5",  # TerraWatt
        "#E15F99",  # Local Partners
        "#1CA71C",  # Precast Facility
        "#9A9A9A",  # Debt Finance
        "#FBC15E",  # Equity Finance
        "#FF9F40",  # University
        "#845EC2",  # Housing REIT
        "#D65DB1"   # Investors
    ]

    # Define links (flows)
    sources = [0, 1, 2, 3, 4, 5, 6]
    targets = [2, 2, 6, 6, 6, 6, 7]
    values =  [4.68, 0.83, 2.0, 4.2, 2.8, 8.0, 8.0]

    # Labels for links (contextual meaning)
    link_labels = [
        "TerraWatt Investment (4.68m)", 
        "Local Equity Share (0.83m)", 
        "Component Supply (2.0m)", 
        "Debt Financing (4.2m)", 
        "Equity Financing (2.8m)", 
        "Lease Payments (8.0m/yr)", 
        "Returns to Investors"
    ]

    # Soft matching link colors
    link_colors = [
        "rgba(46,145,229,0.6)", 
        "rgba(225,95,153,0.6)", 
        "rgba(28,167,28,0.5)", 
        "rgba(154,154,154,0.5)", 
        "rgba(251,193,94,0.5)", 
        "rgba(255,159,64,0.5)", 
        "rgba(132,94,194,0.6)"
    ]

    # Build Sankey
    fig = go.Figure(data=[go.Sankey(
        arrangement="snap",
        node=dict(
            pad=18,
            thickness=22,
            line=dict(color="black", width=0.4),
            label=labels,
            color=colors
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values,
            label=link_labels,
            color=link_colors
        )
    )])

    # Add shaded background rectangles for clarity of layers
    fig.update_layout(
        shapes=[
            # Layer 1 (Production Facility)
            dict(
                type="rect",
                x0=0, y0=0.55, x1=0.4, y1=1,
                line=dict(width=0),
                fillcolor="rgba(46, 145, 229, 0.05)",
                layer="below"
            ),
            # Layer 2 (Housing REIT)
            dict(
                type="rect",
                x0=0.4, y0=0, x1=1, y1=0.55,
                line=dict(width=0),
                fillcolor="rgba(132, 94, 194, 0.05)",
                layer="below"
            )
        ],
        annotations=[
            dict(
                x=0.2, y=1.02,
                text="Layer 1: Production Facility",
                showarrow=False,
                font=dict(size=14, color="black")
            ),
            dict(
                x=0.7, y=0.57,
                text="Layer 2: Housing REIT",
                showarrow=False,
                font=dict(size=14, color="black")
            )
        ],
        title=dict(
            text="<b>Two-Layer Investment Model Structure</b>",
            x=0.5,
            xanchor="center",
            font=dict(size=18)
        ),
        font=dict(size=12),
        margin=dict(l=30, r=30, t=80, b=30),
        plot_bgcolor="white",
        height=600
    )
    
    return fig

# Main app
def main():
    st.title("TerraWatt Finance Model Visualization")
    
    # Create and display the Sankey diagram
    fig = create_sankey()
    st.plotly_chart(fig, use_container_width=True)
    
    # Add space
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Logo section - centered
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.subheader("TerraWatt Engitech Private Limited")
        
        # Try to load the logo (if available)
        try:
            # If you have the logo file in your directory, you can use:
            # logo = Image.open("11.png")
            # st.image(logo, width=300)
            
            # For now, we'll use a placeholder
            st.info("Your logo will appear here when uploaded")
            
            # Instructions for adding the logo
            st.markdown("""
            **To add your logo:**
            1. Upload your logo file to the same directory as this app
            2. Uncomment the logo loading code above
            3. Replace "TEIPL_FINAL_LOGO_11.png" with your actual filename
            """)
        except:
            st.info("Logo will appear here once properly configured")

# Run the app
if __name__ == "__main__":

    main()
