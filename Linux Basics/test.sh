# question 1

mkdir test_dir
cd test_dir
touch example.txt
mv example.txt renamed_example.txt
ls -al

# question 2

cat /etc/passwd
head -n 5 /etc/passwd
tail -n 5 /etc/passwd

# question 3

cat /etc/passwd | grep "root"

# question 4

zip -r test_dir.zip test_dir
unzip test_dir.zip -d unzipped_dir

# question 5

wget -O file.txt https://example.com/sample.txt
curl -o file.txt https://example.com/sample.txt
wget --content-on-error -O file.txt https://example.com/sample.txt

# question 6

touch secure.txt
sudo chmod 444 secure.txt
ls -al

# question 7
export MY_VAR="Hello, Linux!"
echo $MY_VAR