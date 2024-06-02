# Function to get the current time in [HH:MM] format
function current_time {
    echo "[%D{%H:%M}]"
}

# Function to get the username
function username {
    echo "~ $USER"
}

# Prompt configuration with a newline after the command prompt
PROMPT='$(current_time) $(username) <-> '

# Right Prompt (RPROMPT) is left empty
RPROMPT=''

# Function to print a newline before displaying the prompt

# Disable git prompt and other unused parts for simplicity
ZSH_THEME_GIT_PROMPT_PREFIX=""
ZSH_THEME_GIT_PROMPT_SUFFIX=""
ZSH_THEME_GIT_PROMPT_DIRTY=""
ZSH_THEME_GIT_PROMPT_AHEAD=""
ZSH_THEME_GIT_PROMPT_CLEAN=""

ZSH_THEME_GIT_PROMPT_ADDED=""
ZSH_THEME_GIT_PROMPT_MODIFIED=""
ZSH_THEME_GIT_PROMPT_DELETED=""
ZSH_THEME_GIT_PROMPT_RENAMED=""
ZSH_THEME_GIT_PROMPT_UNMERGED=""
ZSH_THEME_GIT_PROMPT_UNTRACKED=""

# Format for git_prompt_long_sha() and git_prompt_short_sha()
ZSH_THEME_GIT_PROMPT_SHA_BEFORE=""
ZSH_THEME_GIT_PROMPT_SHA_AFTER=""

# Colors for time since commit are not needed
ZSH_THEME_GIT_TIME_SINCE_COMMIT_SHORT=""
ZSH_THEME_GIT_TIME_SHORT_COMMIT_MEDIUM=""
ZSH_THEME_GIT_TIME_SINCE_COMMIT_LONG=""
ZSH_THEME_GIT_TIME_SINCE_COMMIT_NEUTRAL=""

# Remove git_time_since_commit function if not needed
