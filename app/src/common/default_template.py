def gen_default_template():
    return """${"##"} Updated: ${ln_main_date}

${"##"} Info

- Last tag: ${ln_last}
- Released: ${ln_released}

## Versions
% for item in ln_list_versions:
- [Version: ${item['tag']} (${item['date']})](#${item['target']})
% endfor

% for tag in ln_map_commits:
${"##"} Version: ${tag['tag']} (${tag['date']})
    % for group in tag['data']:
        ${"###"} ${group['group']}
        % for commit in group['data']:
            * [${commit['optional'][0]}] ${commit['optional'][1]} ${commit['author']['name']}
        % endfor
    % endfor
% endfor
"""
