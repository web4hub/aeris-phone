bash -lc python - <<'PY'
import ast
print('python ok')
PY
bash -lc rm -rf /tmp/aeris-phone && git clone -q https://github.com/web4hub/aeris-phone.git /tmp/aeris-phone && cd /tmp/aeris-phone && python -m compileall -q . && python -m pytest -q
