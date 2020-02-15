echo "削除対象のファイル:"
git clean -X -n

read -p "削除してよろしいですか？  (y/n) :" YN
if [ "${YN}" = "y" ]; then
    ### do
    git clean -X -f
else
    exit 1;
fi

