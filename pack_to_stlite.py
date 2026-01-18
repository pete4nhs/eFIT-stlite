from stlitepack import pack, setup_github_pages
from stlitepack.pack import get_stlite_versions, list_files_in_folders

get_stlite_versions()

# Add all the files in the provided folders to a list
data_files = list_files_in_folders(
    ["input_data_f", "input_data_ind", "input_data_m", "input_data_other"]
)

# Add some specific additional files to the list
data_files.extend(
    [
        "pages/longer_equation.png",
        "pages/single_equation.png",
        "pages/video_tutorial.mp4",
        "pages/where.png",
        "favicon.ico",
    ]
)

# Check the output
print(data_files)

pack(
    # Pack the tool with efit_tool.py as the entrypoint (main file)
    "efit_tool.py",
    # Only major requirements are plotly
    requirements=["plotly", "pandas"],
    # Embed some additional text-based files directly into the resulting index.html files
    extra_files_to_embed=[".streamlit/config.toml", "indicators_n_pop_data_25_26.py"],
    extra_files_to_link=data_files,
    # Point to a github repo for the linked files
    # (will need to change this to
    # pete4nhs/eFIT-tool
    # when ready)
    prepend_github_path="bergam0t/eFIT-tool-stlitepack",
    # Use the more advanced API that supports linking files, not just embedding
    use_raw_api=True,
    # Play around with the versions of stlite - though best to keep these two parameters
    # the same as each other!
    # From version 0.81.6, there seems to be an issue with st.dataframe not displaying
    # From version 0.77.0 onwards, there is a bug with the display of plotly plots
    # so 0.80.5 seems like the sweet spot at the time of writing (August 2025).
    stylesheet_version="0.80.5",
    js_bundle_version="0.80.5",
    run_preview_server=True,
    # replace_df_with_table=True
)

# Create the associated workflow and .nojekyll files
setup_github_pages(mode="gh-actions", use_docs=True)
