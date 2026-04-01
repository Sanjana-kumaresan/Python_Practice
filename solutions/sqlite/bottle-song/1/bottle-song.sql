WITH RECURSIVE verses(start_bottles, take_down, n, text) AS (
  SELECT
    start_bottles,
    take_down,
    start_bottles,
    ''
  FROM "bottle-song"

  UNION ALL

  SELECT
    start_bottles,
    take_down,
    n - 1,
    text ||
    CASE WHEN text != '' THEN CHAR(10) || CHAR(10) ELSE '' END ||

    -- First line
    (CASE n
      WHEN 10 THEN 'Ten'
      WHEN 9 THEN 'Nine'
      WHEN 8 THEN 'Eight'
      WHEN 7 THEN 'Seven'
      WHEN 6 THEN 'Six'
      WHEN 5 THEN 'Five'
      WHEN 4 THEN 'Four'
      WHEN 3 THEN 'Three'
      WHEN 2 THEN 'Two'
      WHEN 1 THEN 'One'
    END) || ' green bottle' || CASE WHEN n = 1 THEN '' ELSE 's' END || ' hanging on the wall,' || CHAR(10) ||

    -- Second line
    (CASE n
      WHEN 10 THEN 'Ten'
      WHEN 9 THEN 'Nine'
      WHEN 8 THEN 'Eight'
      WHEN 7 THEN 'Seven'
      WHEN 6 THEN 'Six'
      WHEN 5 THEN 'Five'
      WHEN 4 THEN 'Four'
      WHEN 3 THEN 'Three'
      WHEN 2 THEN 'Two'
      WHEN 1 THEN 'One'
    END) || ' green bottle' || CASE WHEN n = 1 THEN '' ELSE 's' END || ' hanging on the wall,' || CHAR(10) ||

    -- Third line
    'And if one green bottle should accidentally fall,' || CHAR(10) ||

    -- Fourth line
    'There''ll be ' ||
    CASE 
      WHEN n - 1 = 0 THEN 'no green bottles hanging on the wall.'
      WHEN n - 1 = 1 THEN 'one green bottle hanging on the wall.'
      ELSE
        (CASE n - 1
          WHEN 10 THEN 'ten'
          WHEN 9 THEN 'nine'
          WHEN 8 THEN 'eight'
          WHEN 7 THEN 'seven'
          WHEN 6 THEN 'six'
          WHEN 5 THEN 'five'
          WHEN 4 THEN 'four'
          WHEN 3 THEN 'three'
          WHEN 2 THEN 'two'
        END) || ' green bottles hanging on the wall.'
    END
  FROM verses
  WHERE n > start_bottles - take_down
)

UPDATE "bottle-song"
SET result = (
  SELECT text
  FROM verses v
  WHERE v.start_bottles = "bottle-song".start_bottles
    AND v.take_down = "bottle-song".take_down
    AND v.n = "bottle-song".start_bottles - "bottle-song".take_down
);