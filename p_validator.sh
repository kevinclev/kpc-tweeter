not_p=()

# Make sure each definition starts with a P
while read line
  do
    initial="$(echo $line | head -c 1)"
    if [[ $initial != "P" ]];then
      echo "$line does not start with a P"
      not_p+=("$line")
    fi
done < definitions.txt

if [ ${#not_p[@]} -ne 0 ];then
echo "Incorrect definitions:"
  for i in "${not_p[@]}"
    do
      echo $i
  done
  exit 1
fi

# Check for duplicates
dupes=`sort definitions.txt | uniq -d`

if [ ! -z "$dupes" ];then
  echo "There are duplicate values!"
  echo $dupes
  exit 1
fi
