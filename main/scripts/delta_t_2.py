"""
Time interval extraction script
Copyright (C) 2022  Abhinav M

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

"""



def timeDiff(t_2, t_1):
    h1, m1, s1 = t_1.split(':')
    h2, m2, s2 = t_2.split(':')
    diff = 3600*((int(h2)-int(h1))%24) + 60*(int(m2)-int(m1)) + (int(s2) - int(s1))

    return str(diff)

with open("./data/delta_t", 'w') as diffs:
    with open("./data/start_times") as f:
        previous_time = "0:0:0"
        first_iteration = True

        for line in f:
            current_time = line.strip().split()[2]
            #print(current_time)
            difference = timeDiff(current_time, previous_time)
            print(previous_time, current_time, difference)
            previous_time = current_time

            if not first_iteration:
                diffs.write(difference+'\n')

            first_iteration = False # skip the first loop
